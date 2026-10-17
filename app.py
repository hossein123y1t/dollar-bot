export default {
  async scheduled(event, env) {
    await send(env);
  }
};

async function send(env) {
  const t = env.TELEGRAM_TOKEN;
  const c = env.TELEGRAM_CHAT_ID;
  const r = await fetch("https://api.priceto.day/v1/latest/irr/usd");
  const d = await r.json();
  const m = "قیمت دلار: " + (d.price / 10).toLocaleString() + " تومان";
  
  await fetch("https://api.telegram.org/bot" + t + "/sendMessage", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ chat_id: c, text: m })
  });
}
