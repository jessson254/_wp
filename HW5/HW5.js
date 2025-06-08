import { Application } from "https://deno.land/x/oak/mod.ts";

const app = new Application();

app.use((ctx) => {
  console.log('url =', ctx.request.url);
  const pathname = ctx.request.url.pathname;

  if (pathname === '/') {
    ctx.response.headers.set("Content-Type", "text/html; charset=utf-8");
    ctx.response.body = `
      <!DOCTYPE html>
      <html lang="zh">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>我的自我介紹</title>
          <style>
              body { font-family: Arial, sans-serif; text-align: center; margin: 50px; }
              h1 { color: #333; }
              ol { list-style: none; padding: 0; }
              li { margin: 10px 0; }
              a { text-decoration: none; color: #007BFF; font-weight: bold; }
              a:hover { color: #0056b3; }
          </style>
      </head>
      <body>
          <h1>我的自我介紹</h1>
          <ol>
              <li><a href="/name">姓名</a></li>
              <li><a href="/age">年齡</a></li>
              <li><a href="/gender">性別</a></li>
          </ol>
      </body>
      </html>
    `;
  } else if (pathname === '/name') {
    ctx.response.body = '方奕皓';
  } else if (pathname === '/age') {
    ctx.response.body = '18歲';
  } else if (pathname === '/gender') {
    ctx.response.body = '男';
  } else {
    ctx.response.status = 404;
    ctx.response.body = '404 - 找不到頁面';
  }
});

console.log('start at : http://127.0.0.1:8000');
await app.listen({ port: 8000 });
