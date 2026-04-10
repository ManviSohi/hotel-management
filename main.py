# ============================================================
#  GrandStay Hotel — Backend Server (main.py)
#  Python Flask app with chatbot API using if / elif / else
# ============================================================

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from the frontend


# ============================================================
#  HOTEL CHATBOT RESPONSE LOGIC  (if / elif / else)
# ============================================================

def get_chatbot_response(user_message: str) -> str:
    """
    Processes user message and returns appropriate hotel response.
    Uses if / elif / else statements (Python equivalent of JS if/else-if/else).
    """
    msg = user_message.lower().strip()

    # ── 1. GREETINGS ─────────────────────────────────────────
    if "hello" in msg or "hi" in msg or "hey" in msg or "namaste" in msg:
        return (
            "Namaste! 🙏 Welcome to GrandStay Hotel Concierge Service.\n"
            "How may I assist you today?\n\n"
            "I can help with rooms, pricing, check-in/out, amenities, and more!"
        )
 
    # ── 2. ROOM AVAILABILITY ─────────────────────────────────
    elif "availab" in msg or "vacancy" in msg or "book" in msg or "room available" in msg:
        return (
            "🛏️ Current availability at GrandStay:\n\n"
            "  • Deluxe Suite       — ₹8,500 / night\n"
            "  • Presidential Suite — ₹22,000 / night\n"
            "  • Garden Villa       — ₹35,000 / night\n\n"
            "To make a reservation, call +91 11 4567 8900\n"
            "or email reservations@grandstay.in"
        )

    # ── 3. ROOM PRICING ──────────────────────────────────────
    elif "price" in msg or "cost" in msg or "rate" in msg or "tariff" in msg or "charge" in msg:
        return (
            "💰 GrandStay Room Rates:\n\n"
            "  🏷️  Deluxe Suite       — ₹8,500  / night\n"
            "  🏷️  Presidential Suite — ₹22,000 / night\n"
            "  🏷️  Garden Villa       — ₹35,000 / night\n\n"
            "All rates include complimentary breakfast & Wi-Fi.\n"
            "GST applicable at checkout."
        )

    # ── 4. CHECK-IN ───────────────────────────────────────────
    elif "check-in" in msg or "check in" in msg or "checkin" in msg or "arrival" in msg:
        return (
            "🕑 Check-in Time: 2:00 PM\n\n"
            "Early check-in (from 10:00 AM) is available on request\n"
            "at ₹1,000 extra, subject to room availability.\n"
            "Please inform us 24 hours in advance."
        )

    # ── 5. CHECK-OUT ──────────────────────────────────────────
    elif "check-out" in msg or "check out" in msg or "checkout" in msg or "departure" in msg:
        return (
            "🕑 Check-out Time: 11:00 AM\n\n"
            "Late check-out (until 2:00 PM) is available for ₹1,500 extra,\n"
            "subject to availability. Please request at the front desk."
        )

    # ── 6. BREAKFAST / DINING ────────────────────────────────
    elif "breakfast" in msg or "meal" in msg or "dining" in msg or "food" in msg or "restaurant" in msg:
        return (
            "🍳 Dining at GrandStay:\n\n"
            "  ✅ Complimentary breakfast with all room types (7 AM – 10:30 AM)\n"
            "  🍽️  Menu: Indian, Continental & Live Egg Station\n\n"
            "  The Spire Rooftop Restaurant:\n"
            "  • Lunch: 12:00 PM – 3:00 PM\n"
            "  • Dinner: 7:00 PM – 11:00 PM\n"
            "  • Rooftop Bar: 5:00 PM – 12:00 AM"
        )

    # ── 7. AMENITIES ─────────────────────────────────────────
    elif "ameniti" in msg or "facilities" in msg or "spa" in msg or "gym" in msg or "pool" in msg or "wifi" in msg:
        return (
            "✨ GrandStay Amenities:\n\n"
            "  🏊  Heated rooftop pool\n"
            "  💆  Luxury spa & wellness centre\n"
            "  🏋️   24-hr fitness centre\n"
            "  📶  High-speed complimentary Wi-Fi\n"
            "  🚗  Valet parking (complimentary)\n"
            "  👔  24/7 concierge & butler service\n"
            "  🛁  Jacuzzi in Presidential Suite & Garden Villa"
        )

    # ── 8. CANCELLATION ──────────────────────────────────────
    elif "cancel" in msg or "refund" in msg or "policy" in msg:
        return (
            "📋 Cancellation Policy:\n\n"
            "  ✅  Free cancellation — up to 48 hours before check-in\n"
            "  ⚠️   50% charge — cancellation within 24–48 hours\n"
            "  ❌  No refund — within 24 hours or no-show\n\n"
            "Group bookings (5+ rooms) require a 7-day notice."
        )

    # ── 9. LOCATION / DIRECTIONS ─────────────────────────────
    elif "location" in msg or "address" in msg or "direction" in msg or "where" in msg or "airport" in msg:
        return (
            "📍 GrandStay Hotel\n"
            "   12, Palace Road, New Delhi — 110001\n\n"
            "  🚖  IGI Airport → Hotel: ~25 mins (18 km)\n"
            "  🚇  Nearest Metro: Patel Chowk (Blue Line) — 5 min walk\n"
            "  🚌  Free airport shuttle — book 24 hrs in advance\n"
            "  🚗  Complimentary valet parking on arrival"
        )

    # ── 10. PARKING ──────────────────────────────────────────
    elif "parking" in msg or "valet" in msg or "car" in msg or "vehicle" in msg:
        return (
            "🚗 Parking at GrandStay:\n\n"
            "  • Complimentary valet parking for all guests\n"
            "  • Self-park basement: ₹300 / day\n"
            "  • EV charging stations available\n"
            "  • Valet available 24/7 at the main porch"
        )

    # ── 11. PET POLICY ───────────────────────────────────────
    elif "pet" in msg or "dog" in msg or "cat" in msg or "animal" in msg:
        return (
            "🐾 Pet Policy:\n\n"
            "We are a pet-friendly hotel!\n"
            "  • Small pets (under 10 kg) welcome in Garden Villa\n"
            "  • Pet fee: ₹800 per night\n"
            "  • Pet bed & bowls provided on request\n"
            "  • Please inform us at time of booking"
        )

    # ── 12. EVENTS / WEDDING / CONFERENCE ────────────────────
    elif "event" in msg or "wedding" in msg or "conference" in msg or "banquet" in msg or "meeting" in msg:
        return (
            "🎊 Events & Banqueting:\n\n"
            "  • Grand Ballroom    — up to 500 guests\n"
            "  • Conference Hall   — up to 80 delegates\n"
            "  • Garden Lawn       — outdoor events, 300 guests\n\n"
            "For quotes & bookings:\n"
            "  📧  events@grandstay.in\n"
            "  📞  +91 11 4567 8901"
        )

    # ── 13. CONTACT ──────────────────────────────────────────
    elif "contact" in msg or "phone" in msg or "call" in msg or "email" in msg or "number" in msg:
        return (
            "📞 Contact GrandStay Hotel:\n\n"
            "  📱  Phone  : +91 11 4567 8900\n"
            "  📧  Email  : reservations@grandstay.in\n"
            "  🌐  Website: www.grandstay.in\n"
            "  📍  Address: 12, Palace Road, New Delhi\n\n"
            "  ⏰  Front Desk: Open 24 hours / 7 days"
        )

    # ── 14. THANK YOU ────────────────────────────────────────
    elif "thank" in msg or "thanks" in msg or "great" in msg or "awesome" in msg or "helpful" in msg:
        return (
            "It's our pleasure! 🙏\n"
            "At GrandStay, your satisfaction is our highest priority.\n\n"
            "Is there anything else I can help you with?"
        )

    # ── 15. BYE ──────────────────────────────────────────────
    elif "bye" in msg or "goodbye" in msg or "see you" in msg or "exit" in msg:
        return (
            "Goodbye! 🌟\n"
            "Thank you for choosing GrandStay Hotel.\n"
            "We look forward to welcoming you soon. Have a wonderful day!"
        )

    # ── 16. DEFAULT FALLBACK ─────────────────────────────────
    else:
        return (
            "I'm sorry, I didn't quite understand that. 😊\n\n"
            "You can ask me about:\n"
            "  • Room availability & pricing\n"
            "  • Check-in / Check-out timings\n"
            "  • Breakfast & restaurant hours\n"
            "  • Hotel amenities & facilities\n"
            "  • Cancellation & refund policy\n"
            "  • Location & parking\n"
            "  • Events, weddings & conferences\n"
            "  • Contact information"
        )


# ============================================================
#  FLASK ROUTES
# ============================================================

@app.route("/", methods=["GET"])
def home():
    """Serve a simple status page."""
    return jsonify({
        "status": "running",
        "hotel": "GrandStay Hotel",
        "api_endpoint": "/chat [POST]",
        "example_payload": {"message": "What are your room prices?"}
    })


@app.route("/chat", methods=["POST"])
def chat():
    """
    POST /chat
    Body: { "message": "user text here" }
    Returns: { "reply": "bot response", "status": "ok" }
    """
    data = request.get_json(silent=True)

    if not data or "message" not in data:
        return jsonify({
            "reply": "Please provide a 'message' field in the JSON body.",
            "status": "error"
        }), 400

    user_message = data["message"]

    if not isinstance(user_message, str) or not user_message.strip():
        return jsonify({
            "reply": "Message cannot be empty.",
            "status": "error"
        }), 400

    reply = get_chatbot_response(user_message)

    return jsonify({
        "reply": reply,
        "status": "ok",
        "hotel": "GrandStay Hotel"
    })


@app.route("/rooms", methods=["GET"])
def get_rooms():
    """Returns list of available rooms as JSON."""
    rooms = [
        {
            "id": 1,
            "name": "Deluxe Suite",
            "price_per_night": 8500,
            "size_sqm": 45,
            "bed": "King",
            "view": "City",
            "amenities": ["Wi-Fi", "Breakfast", "AC", "Smart TV", "Mini Bar"]
        },
        {
            "id": 2,
            "name": "Presidential Suite",
            "price_per_night": 22000,
            "size_sqm": 120,
            "bed": "Super King",
            "view": "Panoramic",
            "amenities": ["Wi-Fi", "Breakfast", "Butler", "Jacuzzi", "Private Dining"]
        },
        {
            "id": 3,
            "name": "Garden Villa",
            "price_per_night": 35000,
            "size_sqm": 200,
            "bed": "Super King",
            "view": "Garden",
            "amenities": ["Wi-Fi", "Breakfast", "Private Pool", "Butler", "Jacuzzi", "Outdoor Deck"]
        }
    ]
    return jsonify({"rooms": rooms, "total": len(rooms)})


@app.route("/contact", methods=["GET"])
def get_contact():
    """Returns hotel contact information."""
    return jsonify({
        "hotel": "GrandStay Hotel",
        "address": "12, Palace Road, New Delhi — 110001",
        "phone": "+91 11 4567 8900",
        "email": "reservations@grandstay.in",
        "website": "www.grandstay.in",
        "checkin": "2:00 PM",
        "checkout": "11:00 AM",
        "front_desk": "24/7"
    })


# ============================================================
#  RUN SERVER
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("  GrandStay Hotel — Backend Server")
    print("  Running on http://localhost:5000")
    print("  POST /chat  to use the chatbot API")
    print("=" * 50)
    app.run(debug=True, port=5000)
