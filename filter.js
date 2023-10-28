const dayjs = require("dayjs");
const patients = require("./patients.json");
const fs = require("fs");
const customParse = require("dayjs/plugin/customParseFormat");
dayjs.extend(customParse);

const patientFilterd = patients.map((patient) => {
  const patientObj = { ...patient };
  patientObj.Evolution = [];
  patientObj.additionalInfo = patient.words;

  patientObj.birthdate = convertToFullYear(patient.birthdate);
  const mobile = fixNumber(patient.mobile);
  const phone = fixNumber(patient.phone);

  if (mobile || phone) {
    if (mobile?.isPhone) {
      if (phone && phone.isPhone) {
        patientObj.mobile = null;
      } else {
        patientObj.mobile = phone?.number;
      }
    } else {
      patientObj.mobile = mobile?.number;
    }
    if (phone?.isPhone) {
      patientObj.phone = phone?.number;
    } else {
      if (mobile && mobile.isPhone) {
        patientObj.phone = mobile.number;
      } else {
        patientObj.phone = null;
      }
    }
  } else {
    patientObj.mobile = null;
    patientObj.phone = null;
  }

  if (patientObj.prontuario) {
    patientObj.Evolution.push(
      ...splitStringByDateAndDescription(patientObj.prontuario)
    );
  }
  if (patientObj.prontuario2) {
    patientObj.Evolution.push(
      ...splitStringByDateAndDescription(patientObj.prontuario2)
    );
  }

  delete patientObj.prontuario;
  delete patientObj.prontuario2;
  delete patientObj.words;

  //   const splittedProntuario = patientObj.prontuario.split("\n");
  //   splittedProntuario.forEach((p) => {
  //     const data = p.substr(0, 10);
  //     const desc = p.substr(11, p.length);
  //     if (data === "" || desc === "") return;
  //     patientObj.Evolution.push({
  //       createdAt: data,
  //       description: desc,
  //     });
  //   });
  return patientObj;
});

fs.writeFile(
  "./patients-fixed.json",
  JSON.stringify(patientFilterd),
  "utf8",
  (err) => {
    console.log(err);
  }
);

function splitStringByDateAndDescription(text) {
  const inputString = text.replaceAll("\\", "/");
  const datePattern = /(\d{1,2}\/\d{1,2}\/\d{2,4})/g;
  const dateMatches = inputString.match(datePattern);

  // Split the string by date patterns and keep non-empty parts
  const parts = inputString.split(datePattern);

  if (!dateMatches || !parts) {
    return [];
  }

  // Initialize variables to store the result
  const result = [];
  let i = 1;

  dateMatches.forEach((date, index) => {
    const fixdate = convertToFullYear(date);

    if (date == "2/08/2016") {
      console.log("here", date, fixdate);
    }
    try {
      result.push({
        createdAt: fixdate,
        description: sanitizeString(parts[(index + 1) * 2].trim()),
      });
    } catch (error) {
      console.log("here", error);
    }
  });

  return result;
}

function convertToFullYear(dateString) {
  const dateRegex = /^\d{2}\/\d{2}\/\d{2}$/;

  if (dateRegex.test(dateString)) {
    const dateSplit = dateString.split("/");
    let year = `20${dateSplit[2]}`;
    if (dateSplit[2] > 15) {
      year = `19${dateSplit[2]}`;
    }
    let day = dateSplit[0];

    if (day.length == 1) {
      day = `0${day}`;
    }

    return new Date(year, dateSplit[1] - 1, day);
  } else {
    const dateRegex = /^\d{2}\/\d{2}\/\d{4}$/;
    const dateSplit = dateString.split("/");
    let day = dateSplit[0];

    if (day.length == 1) {
      day = `0${day}`;
    }

    // if (dateRegex.test(dateString)) {
    return new Date(dateSplit[2], dateSplit[1] - 1, day);
    // } else {
    //   return null;
    // }
  }
}

function fixNumber(inputString) {
  if (!inputString) return null;
  const numberFix = inputString.match(/\d+/g)?.join("");
  if (!numberFix) return null;

  const isPhone = numberFix.startsWith("3") || numberFix.startsWith("2");

  if (numberFix.length == 7 || numberFix.length == 8 || numberFix.length == 9) {
    let finalNumber = numberFix;
    if (numberFix.length == 8) {
      if (!isPhone) {
        finalNumber = `9${numberFix}`;
      }
    }
    if (isPhone && numberFix.length == 7) {
      {
        finalNumber = `3${numberFix}`;
      }
    }
    return { number: `55${finalNumber}`, isPhone };
  }

  return null;
}

function sanitizeString(text) {
  // Use regular expression to replace leading periods, colons, and spaces with an empty string
  const removedChars = text.replace(/^[:. ]+/, "");
  const upperCaseFirstLetter =
    removedChars.charAt(0).toUpperCase() +
    removedChars.substring(1, removedChars.length + 1);
  return upperCaseFirstLetter;
}
