#include <cstdio>

#include <iostream>

#include <unordered_map>
#include <bitset>

#include <cassert>

constexpr int N = 2;

// The two leftmost bits are the floor the elevator is on.
using State = uint64_t;
using BT = std::bitset<64>;

constexpr uint8_t HYDROGEN =  0;
constexpr uint8_t LITHIUM = 1 << 0;

constexpr State ELEV_MASK = (State(-1) >> 2);

// Set the elevator floor
constexpr State set_elevator(const State s, const uint8_t floor) {
	return (s & ELEV_MASK) | (State(floor) << 62);
}

// Get the elevator floor
constexpr uint8_t get_elevator(const State s) {
	return (s >> 62);
}

constexpr bool is_gen_on_floor(const State s, const uint8_t floor, const uint8_t gen) {
	const uint8_t idx = floor*N;
	const uint8_t shifty = s >> idx;
	return (shifty & gen);
}

// Get the floor of the elevator.
constexpr uint8_t get_generator(const State s, const uint8_t gen) {
	for (uint8_t i = 0; i < 4; i++) {
		if (is_gen_on_floor(s, i, gen)) {
			return i;
		}
	}
	assert(false);
	return 4;
}

int main() {
	State b1;

	/* auto b2 = set_elevator(b1, 2); */
	auto b2 = set_elevator(b1, 2);
	uint8_t c2 = get_elevator(b2);

	return 0;
}
