 // ============================================================
//  GrandStay Hotel — Chatbot Logic (script.js)
//  Uses if / else-if / else chains (Python: if / elif / else)
// ============================================================

const messagesEl = document.getElementById("chat-messages");
const inputEl    = document.getElementById("chat-input");
const chatbot    = document.getElementById("chatbot");
const toggle     = document.getElementById("chat-toggle");

// ── Toggle chatbot open/close ──────────────────────────────
toggle.addEventListener("click", () => {
  chatbot.classList.toggle("open");
  if (chatbot.classList.contains("open") && messagesEl.children.length === 0) {
    botMessage("Namaste! 🙏 Welcome to GrandStay Hotel Concierge. How may I assist you today?\n\nYou can ask about rooms, pricing, amenities, check-in/out times, and more.");
  }
});

// ── Add a bot message bubble ───────────────────────────────
function botMessage(text) {
  const div = document.createElement("div");
  div.className = "msg bot";
  div.innerText = text;
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

// ── Add a user message bubble ──────────────────────────────
function userMessage(text) {
  const div = document.createElement("div");
  div.className = "msg user";
  div.innerText = text;
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

// ── Send from input field ──────────────────────────────────
function sendMessage() {
  const text = inputEl.value.trim();
  if (!text) return;
  userMessage(text);
  inputEl.value = "";
  fetch("http://localhost:5000/chat", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ message: text })
})
.then(res => res.json())
.then(data => {
  botMessage(data.reply);
})
.catch(() => {
  botMessage("⚠️ Server error. Please try again.");
});
}

// ── Send from quick-reply button ───────────────────────────
function sendQuick(text) {
  userMessage(text);
  fetch("http://localhost:5000/chat", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ message: text })
})
.then(res => res.json())
.then(data => {
  botMessage(data.reply);
})
.catch(() => {
  botMessage("⚠️ Server error. Please try again.");
});
}

// ============================================================
//  MAIN RESPONSE LOGIC  (if / else-if / else  ←→ Python's
//                         if / elif / else)
// ============================================================
function respond(msg) {

  // ── 1. GREETINGS ──────────────────────────────────────────
  if (msg.includes("hello") || msg.includes("hi") || msg.includes("hey") || msg.includes("namaste")) {
    botMessage("Namaste! 🙏 Welcome to GrandStay Hotel. I'm your digital concierge. How can I help you today?");
  }

  // ── 2. ROOM AVAILABILITY ──────────────────────────────────
  else if (msg.includes("availab") || msg.includes("room available") || msg.includes("vacancy") || msg.includes("book")) {
    botMessage("🛏️ We currently have availability in:\n\n• Deluxe Suite — ₹8,500/night\n• Presidential Suite — ₹22,000/night\n• Garden Villa — ₹35,000/night\n\nWould you like to book any of these? Call us at +91 11 4567 8900 or email reservations@grandstay.in");
  }

  // ── 3. ROOM PRICE / RATES ─────────────────────────────────
  else if (msg.includes("price") || msg.includes("cost") || msg.includes("rate") || msg.includes("charge") || msg.includes("fee") || msg.includes("tariff")) {
    botMessage("💰 Our room rates:\n\n🏷️ Deluxe Suite     — ₹8,500 / night\n🏷️ Presidential Suite — ₹22,000 / night\n🏷️ Garden Villa      — ₹35,000 / night\n\nAll rates include complimentary breakfast, Wi-Fi, and access to the fitness center. Taxes are applied at checkout.");
  }

  // ── 4. CHECK-IN TIME ──────────────────────────────────────
  else if (msg.includes("check-in") || msg.includes("check in") || msg.includes("checkin") || msg.includes("arrival")) {
    botMessage("🕑 Check-in time is 2:00 PM.\n\nEarly check-in may be available upon request, subject to room availability. Please inform us at least 24 hours in advance for arrangements.");
  }

  // ── 5. CHECK-OUT TIME ─────────────────────────────────────
  else if (msg.includes("check-out") || msg.includes("check out") || msg.includes("checkout") || msg.includes("departure") || msg.includes("leaving")) {
    botMessage("🕑 Check-out time is 11:00 AM.\n\nLate check-out until 2:00 PM is available for ₹1,500 extra, subject to availability. Please request at the front desk.");
  }

  // ── 6. BREAKFAST ──────────────────────────────────────────
  else if (msg.includes("breakfast") || msg.includes("food included") || msg.includes("meal") || msg.includes("dining")) {
    botMessage("🍳 Yes! Complimentary breakfast is included with all room types.\n\nOur restaurant serves breakfast from 7:00 AM – 10:30 AM. The menu features Indian, Continental, and Live Egg Station options.\n\nFor lunch & dinner, our rooftop restaurant The Spire is open from 12:00 PM – 11:00 PM.");
  }

  // ── 7. AMENITIES ──────────────────────────────────────────
  else if (msg.includes("ameniti") || msg.includes("facilities") || msg.includes("services") || msg.includes("spa") || msg.includes("gym") || msg.includes("pool") || msg.includes("wifi") || msg.includes("wi-fi")) {
    botMessage("✨ GrandStay Hotel Amenities:\n\n🏊 Heated rooftop pool\n💆 Luxury spa & wellness center\n🏋️ 24-hr fitness center\n📶 High-speed complimentary Wi-Fi\n🍽️ 2 restaurants + rooftop bar\n🚗 Valet parking\n👔 Concierge & butler service\n🛁 Jacuzzi in Presidential & Villa rooms");
  }

  // ── 8. CANCELLATION POLICY ────────────────────────────────
  else if (msg.includes("cancel") || msg.includes("refund") || msg.includes("policy")) {
    botMessage("📋 Cancellation Policy:\n\n✅ Free cancellation up to 48 hours before check-in\n⚠️ 50% charge for cancellation within 24–48 hours\n❌ No refund for cancellation within 24 hours or no-show\n\nFor group bookings (5+ rooms), a 7-day cancellation window applies.");
  }

  // ── 9. LOCATION / DIRECTIONS ──────────────────────────────
  else if (msg.includes("location") || msg.includes("address") || msg.includes("direction") || msg.includes("where") || msg.includes("near") || msg.includes("airport")) {
    botMessage("📍 GrandStay Hotel\n12, Palace Road, New Delhi — 110001\n\n🚖 From IGI Airport: ~25 mins (18 km)\n🚇 Nearest Metro: Patel Chowk (Blue Line) — 5 min walk\n🚌 Free airport shuttle available — book 24 hrs in advance");
  }

  // ── 10. PARKING ───────────────────────────────────────────
  else if (msg.includes("parking") || msg.includes("car") || msg.includes("vehicle") || msg.includes("valet")) {
    botMessage("🚗 Parking Options:\n\n• Complimentary valet parking for all guests\n• Self-parking basement: ₹300/day\n• EV charging stations available\n\nOur valet team is available 24/7 at the main porch.");
  }

  // ── 11. PET POLICY ────────────────────────────────────────
  else if (msg.includes("pet") || msg.includes("dog") || msg.includes("cat") || msg.includes("animal")) {
    botMessage("🐾 Pet Policy:\n\nWe are a pet-friendly hotel!\n• Small pets (under 10 kg) welcome in Garden Villa\n• Pet fee: ₹800 per night\n• Pet bed & bowls provided on request\n• Please inform us at booking time");
  }

  // ── 12. EVENTS / WEDDING / CONFERENCE ────────────────────
  else if (msg.includes("event") || msg.includes("wedding") || msg.includes("conference") || msg.includes("banquet") || msg.includes("meeting") || msg.includes("party")) {
    botMessage("🎊 Event & Banquet Services:\n\n• Grand Ballroom — capacity 500 guests\n• Conference Hall — capacity 80 delegates\n• Garden Lawn — outdoor events up to 300 guests\n• Dedicated events team for weddings & corporate functions\n\nFor quotations, email events@grandstay.in or call +91 11 4567 8901");
  }

  // ── 13. CONTACT ───────────────────────────────────────────
  else if (msg.includes("contact") || msg.includes("phone") || msg.includes("email") || msg.includes("call") || msg.includes("number") || msg.includes("reach")) {
    botMessage("📞 Contact GrandStay Hotel:\n\n📱 Phone: +91 11 4567 8900\n📧 Email: reservations@grandstay.in\n🌐 Website: www.grandstay.in\n📍 12, Palace Road, New Delhi\n\n⏰ Front desk: 24 hours / 7 days a week");
  }

  // ── 14. THANK YOU ─────────────────────────────────────────
  else if (msg.includes("thank") || msg.includes("thanks") || msg.includes("great") || msg.includes("awesome") || msg.includes("helpful")) {
    botMessage("It's our pleasure! 🙏 That's what GrandStay Concierge is here for.\n\nIs there anything else I can help you with today?");
  }

  // ── 15. BYE / GOODBYE ────────────────────────────────────
  else if (msg.includes("bye") || msg.includes("goodbye") || msg.includes("see you") || msg.includes("exit") || msg.includes("close")) {
    botMessage("Goodbye! 🌟 Thank you for choosing GrandStay Hotel. We look forward to welcoming you. Have a wonderful day!");
  }

  // ── 16. DEFAULT / FALLBACK ────────────────────────────────
  else {
    botMessage("I'm sorry, I didn't quite understand that. 😊\n\nYou can ask me about:\n• Room availability & pricing\n• Check-in / Check-out times\n• Breakfast & dining\n• Amenities & facilities\n• Cancellation policy\n• Location & parking\n• Events & weddings\n• Contact information");
  }
}
