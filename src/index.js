const { Notion } = require("@neurosity/notion");
require("dotenv").config();

const deviceId = process.env.DEVICE_ID || "";
const email = process.env.EMAIL || "";
const password = process.env.PASSWORD || "";

const verifyEnvs = (email, password, deviceId) => {
    const invalidEnv = (env) => {
        return env === "" || env === 0;
    };
    if (
        invalidEnv(email) ||
        invalidEnv(password) ||
        invalidEnv(deviceId)
    ) {
        console.error(
        "Please verify deviceId, email and password are in .env file, quitting..."
        );
        process.exit(0);
    }
};


verifyEnvs(email, password, deviceId);
console.log(`${email} attempting to authenticate to ${deviceId}`);

//create notion session for the crown
const notion = new Notion({
    deviceId
});



const main = async () => {
    await notion
      .login({
        email,
        password
      })
      .catch((error) => {
        console.log(error);
        throw new Error(error);
      });
    console.log("Logged in");
  };

//logging into the API
main();

const endSession = async () => {
    /*stopping the subscription and emission of data events
    which come from the crown
    */
    subscription.unsubscribe();
    console.log("Exiting...");

    process.exit();
}

/*
Code starts the crown and if the user is calm, then
Hello World is printed.
notion.calm().subscribe((calm) => {
if (calm.probability > 0.3) {
    console.log("Hello World!");
}
});*/

const fs = require('fs');
datapoints = new Array();
//creates a subscription for raw data emission from the crown.
const subscription = notion.brainwaves("raw").subscribe((brainwaves) => {

    datapoints.push(brainwaves)
});

const readline = require('readline');
readline.emitKeypressEvents(process.stdin);
process.stdin.setRawMode(true);
process.stdin.on('keypress', (str, key) => {
  if ((key.ctrl && key.name === 'c') || key.name === 'escape') {
    /*stopping the subscription and emission of data events
    which come from the crown
    */
    txt_data = JSON.stringify(datapoints, null, "\t")
    fs.writeFileSync('../res/training_data/test.json', txt_data);
    setTimeout(endSession, 1000);
  }
});

console.log('Press escape to stop stream...');