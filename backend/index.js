const fs = require('fs');
const path = require('path');
const axios = require('axios');
const { Builder, By, until } = require('selenium-webdriver');
require('chromedriver');

async function getImgs(link, platform) {
  const driver = await new Builder().forBrowser('chrome').build();

  // Configurations
  const platforms = {
    gumtree: {
      parentXPath: '/html/body/div[2]/div[1]/div/main/div[3]',
      acceptButton: true,
      acceptXPath: '/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/button[1]',
    },
    autotrader: {
      parentXPath: '/html/body/div[2]/main',
      acceptButton: true,
      acceptXPath: '/html/body/div/div[2]/div[4]/button[3]',
    },
    ebay: {
      parentXPath: '/html/body/div[2]/main/div[1]/div[1]/div[4]',
      acceptButton: false,
    },
    motors: {
      parentXPath: '/html/body/section/section',
      acceptButton: false,
    },
    cargurus: {
      parentXPath: '/html/body/main/div[2]/div/div[2]/div[2]/div/div',
      acceptButton: false,
    },
    heycar: {
      parentXPath: '/html/body/div[1]/div[1]/main/div[2]/div[1]/div[1]/div[1]/div',
      acceptButton: true,
      acceptXPath: '/html/body/div[3]/div/div/div/div[2]/div/button[2]',
    },
    aa: {
      parentXPath: '/html/body/div[1]/div[3]/main/div[3]/div[1]/div[2]/div[1]/div[1]/div/div/div[1]',
      acceptButton: true,
      acceptXPath: '/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[3]',
    },
    exchangeandmart: {
      parentXPath: '/html/body/div[3]/div/div/form[1]/div[3]/div[1]/div[1]/div/div/div[2]/div[1]',
      acceptButton: true,
      acceptXPath: '/html/body/div/div[2]/div[6]/button[2]',
    },
  };

  const config = platforms[platform];

  try {
    await driver.get(link);

    // Accept cookies if required
    if (config.acceptButton) {
      try {
        const button = await driver.wait(
          until.elementLocated(By.xpath(config.acceptXPath)),
          2000
        );
        await driver.wait(until.elementIsVisible(button), 2000);
        await button.click();
      } catch {
        console.log("didn't need to accept");
      }
    }

    // Scroll to ensure lazy images load
    await driver.executeScript('window.scrollTo(0, document.body.scrollHeight);');
    await driver.sleep(2000);

    // Collect image elements
    const imageElements = await driver.findElements(By.xpath(`${config.parentXPath}//img`));
    const imgUrls = [];

    for (const img of imageElements) {
      let url =
        (await img.getAttribute('src')) ||
        (await img.getAttribute('data-src')) ||
        (await img.getAttribute('srcset'));

      if (url) {
        if (url.includes(',')) {
          url = url.split(',')[0].split(' ')[0];
        }
        imgUrls.push(url);
      }
    }

    // Create image folder
    const folder = path.join(__dirname, 'car_images');
    if (fs.existsSync(folder)) {
      fs.rmSync(folder, { recursive: true });
    }
    fs.mkdirSync(folder);

    console.log(imgUrls);

    // Download and save images
    for (let i = 0; i < imgUrls.length; i++) {
      try {
        const response = await axios.get(imgUrls[i], { responseType: 'arraybuffer' });
        fs.writeFileSync(path.join(folder, `image_${i + 1}.jpg`), response.data);
        console.log(`✅ Saved image_${i + 1}.jpg`);
      } catch (err) {
        console.log(`❌ Failed to download ${imgUrls[i]}: ${err.message}`);
      }
    }
  } finally {
    await driver.quit();
  }
}

// 🔽 Example run
getImgs("https://heycar.com/uk/auto/audi-a1-2022-25-tfsi-sport-5dr-s-tronic-6a4caec2", "heycar");
