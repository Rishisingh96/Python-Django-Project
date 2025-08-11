const seatLayout = document.getElementById("seatLayout");
const count = document.getElementById("count");
const total = document.getElementById("total");
const ticketPrice = 200; // ₹ per seat

// Generate seats dynamically
for (let i = 0; i < 72; i++) {
  const seat = document.createElement("div");
  seat.classList.add("seat");

  // Randomly make some seats occupied
  if (Math.random() < 0.2) {
    seat.classList.add("occupied");
  }

  seat.addEventListener("click", () => {
    if (!seat.classList.contains("occupied")) {
      seat.classList.toggle("selected");
      updateSelectedCount();
    }
  });

  seatLayout.appendChild(seat);
}

function updateSelectedCount() {
  const selectedSeats = document.querySelectorAll(".seat.selected");
  const selectedCount = selectedSeats.length;
  count.innerText = selectedCount;
  total.innerText = selectedCount * ticketPrice;
}

function confirmBooking() {
  const selectedSeats = document.querySelectorAll(".seat.selected");
  if (selectedSeats.length === 0) {
    alert("Please select at least one seat.");
  } else {
    alert(
      `Booking Confirmed!\nSeats: ${selectedSeats.length}\nTotal: ₹${
        selectedSeats.length * ticketPrice
      }`
    );
  }
}
