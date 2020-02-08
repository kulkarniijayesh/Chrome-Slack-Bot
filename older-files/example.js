const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.connect({browserWSEndpoint:"ws://127.0.0.1:9222/devtools/browser/839d03fa-718d-472c-9ad9-cda4d5c842ed"});
  const page = await browser.newPage();
  await page.goto('https://www.youtube.com/watch?v=lhZOFUY1weo');
  //await page.screenshot({path: 'example.png'});
  await page.keyboard.press(' ');
  //await browser.close();
})();
