function makeCall() {
  const name = document.getElementById("name").value;
  const phoneNumber = document.getElementById("phoneNumber").value;
  const jobTitle = document.getElementById("jobTitle").value;
  const jobLocation = document.getElementById("jobLocation").value;
  const hourlyRate = document.getElementById("hourlyRate").value;
  const jobType = document.getElementById("jobType").value;
  const remote = document.getElementById("remote").value;
  const requiredSkills = document.getElementById("requiredSkills").value;
  const recruiterName = document.getElementById("recruiterName").value;
  const recruiterPhone = document.getElementById("recruiterPhone").value;
  const recruiterEmail = document.getElementById("recruiterEmail").value;

  const modelId = "1707142827149x519497455730688000";

  const options = {
    method: "POST",
    headers: {
      accept: "application/json",
      "content-type": "application/json",
      Authorization: "Bearer 1704476529550x370244089367633100",
    },
    body: JSON.stringify({
      model: modelId,
      phone: phoneNumber,
      name: name,
      custom_variables: [
        `job_title: ${jobTitle}`,
        `job_location: ${jobLocation}`,
        `hourly_rate: ${hourlyRate}`,
        `job_type: ${jobType}`,
        `remote: ${remote}`,
        `required_skills: ${requiredSkills}`,
        `recruiter_name: ${recruiterName}`,
        `recruiter_phone: ${recruiterPhone}`,
        `recruiter_email: ${recruiterEmail}`,
      ],
    }),
  };

  const apiUrl = "/api/call"; // Adjust the route according to your Flask app

  fetch(apiUrl, options)
    .then((response) => response.json())
    .then((data) => {
      displayOutput(data);
    })
    .catch((error) => {
      console.error("Error making API call:", error);
      displayOutput({ status: "error", response: error.message });
    });
}

function displayOutput(data) {
  const outputDiv = document.getElementById("output");
  outputDiv.innerHTML = `
            <p>Status: ${data.status}</p>
            <p>Response: ${JSON.stringify(data.response)}</p>
        `;
}

function makeMultipleCalls() {
  const customVariables = {
    jobTitle: document.getElementById("jobTitle").value,
    jobLocation: document.getElementById("jobLocation").value,
    hourlyRate: document.getElementById("hourlyRate").value,
    jobType: document.getElementById("jobType").value,
    remote: document.getElementById("remote").value,
    requiredSkills: document.getElementById("requiredSkills").value,
    recruiterName: document.getElementById("recruiterName").value,
    recruiterPhone: document.getElementById("recruiterPhone").value,
    recruiterEmail: document.getElementById("recruiterEmail").value,
  };

  const file = document.getElementById("file").files[0];
  const reader = new FileReader();

  reader.onload = (event) => {
    const csvData = event.target.result;
    const csvJson = convertCsvToJson(csvData);

    const jsonData = JSON.stringify({
      file: csvJson,
      custom_variables: customVariables,
    });

    const formData = new FormData();
    formData.append("file", new Blob([jsonData], { type: "application/json" }));

    fetch("/api/make-multiple-calls", {
      method: "POST",
      body: formData,
      headers: {
        Accept: "application/json",
        Authorization: "Bearer 1704476529550x370244089367633100",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        displayOutput(data);
      })
      .catch((error) => {
        console.error("Error making API call:", error);
        displayOutput({ status: "error", response: error.message });
      });
  };

  reader.readAsText(file);
}

function convertCsvToJson(csvData) {
  const lines = csvData.trim().split("\n");
  const headers = lines[0].split(",");
  const jsonData = [];

  for (let i = 1; i < lines.length; i++) {
    const obj = {};
    const currentLine = lines[i].split(",");

    for (let j = 0; j < headers.length; j++) {
      obj[headers[j]] = currentLine[j].replace(/\r/g, "");
    }

    jsonData.push(obj);
  }

  return jsonData;
}
