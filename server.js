var express = require('express');
var app = express();
const http = require('http')

const puppeteer = require('puppeteer-core');
browser_connection = "";
page_global = "";
data = "";
ws_url = "";

http.get('http://127.0.0.1:9222/json/version',(resp)=>{
	resp.on('data', (chunk) => {
   		 data += chunk;
 	 });
	resp.on('end', () => {
    		//console.log(JSON.parse(data));
		ws_url = (JSON.parse(data)).webSocketDebuggerUrl;
		console.log(ws_url);
 	 });
});

app.set('port', 5000);
app.get('/',(req, res)=>{
	res.setHeader('Content-Type','text/html');
    	res.write("<center><h2>Node js server -- Running</h2></center><br/>");
	res.write("<h4></br>API:</h4>");
	res.end();

});

app.get('/youtube', (req,res)=>{
	(async () => {
  			const browser = await puppeteer.connect({browserWSEndpoint:ws_url});
  			const page = await browser.newPage();
			await page.setViewport({ width: 1366, height: 768});
			page_global = page;		
			url = req.query.url;
  			await page.goto(url);
			page_global.keyboard.press('f');

  			})();
	console.log('page: '+ page_global);
	res.end();	
});

app.get('/space', (req,res)=>{
	console.log('page: '+ page_global);
	page_global.keyboard.press(' ');
	res.end();

});

app.listen(app.get('port'),function(){
    console.log("Server is running on port: "+app.get('port'));
});
