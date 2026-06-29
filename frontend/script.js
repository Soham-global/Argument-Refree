const API_URL = "http://127.0.0.1:8000/verdict";

async function getVerdict() {
  const person1 = document.getElementById("person1").value.trim();
  const person2 = document.getElementById("person2").value.trim();
  const btn     = document.getElementById("judgeBtn");
  const btnText = document.getElementById("btnText");
  const result  = document.getElementById("result");
  const verdict = document.getElementById("verdictText");
  const error   = document.getElementById("error");

  // ── Validation ──────────────────────────────────────────────────
  if (!person1 || !person2) {
    showError("Both sides need to state their argument first.");
    return;
  }

  // ── Loading state ───────────────────────────────────────────────
  btn.disabled    = true;
  btnText.textContent = "⏳ Judging...";
  result.classList.add("hidden");
  error.classList.add("hidden");

  // ── API Call ────────────────────────────────────────────────────
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ person1, person2 }),
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();

    // ── Render verdict ──────────────────────────────────────────
    verdict.textContent = data.verdict;
    result.classList.remove("hidden");

  } catch (err) {
    showError(`Something went wrong: ${err.message}`);
  } finally {
    btn.disabled        = false;
    btnText.textContent = "⚖️ Judge It";
  }
}

function showError(message) {
  const error = document.getElementById("error");
  error.textContent = `⚠️ ${message}`;
  error.classList.remove("hidden");
}