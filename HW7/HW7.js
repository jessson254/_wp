import { Application, Router } from "https://deno.land/x/oak/mod.ts";
import * as view from './render.js'; // 請確保這個檔案存在

const articles = [
  { id: 0, title: "A Peaceful Mind", body: "Living mindfully every day.", created_at: new Date().toISOString() },
  { id: 1, title: "On Growth", body: "Improving a bit every day leads to big results.", created_at: new Date().toISOString() }
];

const router = new Router();

router
  .get("/", showList)
  .get("/article/new", showForm)
  .get("/article/:id", viewArticle)
  .post("/article", saveArticle);

const app = new Application();
app.use(router.routes());
app.use(router.allowedMethods());

async function showList(ctx) {
  ctx.response.body = await view.list(articles);
}

async function showForm(ctx) {
  ctx.response.body = await view.newArticle();
}

async function viewArticle(ctx) {
  const id = parseInt(ctx.params.id, 10);
  const article = articles.find(a => a.id === id);
  if (!article) ctx.throw(404, "Article not found.");
  ctx.response.body = await view.detail(article);
}

async function saveArticle(ctx) {
  const body = ctx.request.body({ type: "form" });
  const data = await body.value;
  const newArticle = {};

  for (const [key, value] of data.entries()) {
    newArticle[key] = value;
  }

  if (!newArticle.title || !newArticle.body) {
    ctx.throw(400, "Title and body are required.");
  }

  const id = articles.length > 0 ? Math.max(...articles.map(a => a.id)) + 1 : 0;
  newArticle.id = id;
  newArticle.created_at = new Date().toISOString();

  articles.push(newArticle);

  ctx.response.redirect("/");
}

console.log("Server is running on http://127.0.0.1:8000");
await app.listen({ port: 8000 });
