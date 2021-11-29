#include <stdio.h>
#include <stdint.h>

int64_t solve() {
	int64_t b = 0;
	int64_t c = 0;
	int64_t d = 0;
	int64_t e = 0;
	int64_t f = 0;
	int64_t g = 0;
	int64_t h = 0;


	b = 105700; //(57 * 100) + 100000;
	c = 122700; // b + 17000

	while (1) { // L8
		f = 1;
		d = 2;
		e = 2;

		do {
			e = d;
			do {
				if ((d*e) == b) {
					f = 0;
					goto done;
				}
				e++;
			} while ((d*e) <= b); // End of l11

			d++;
		} while ((d*2) <= b); // End of l10
done:

		if (f == 0) {
			h += 1;
			/* printf("Intermedit: %ld\n", h); */
		}

		if (b == c) {
			break;
		}

		b += 17;
	} // End of L8

	return h;
}

int64_t disas() {
	int64_t a = 1;
	int64_t b = 0;
	int64_t c = 0;
	int64_t d = 0;
	int64_t e = 0;
	int64_t f = 0;
	int64_t g = 0;
	int64_t h = 0;


	b = 105700; //(57 * 100) + 100000;
	c = 122700; // b + 17000
L8:
	/* printf("a: %ld b: %ld c: %ld d: %ld e: %ld f: %ld g: %ld  h: %ld\n", a, b, c, d, e, f, g, h); */
	f = 1;
	d = 2;
L10:
	e = 2;
L11:
	if ((d * e) == b) {
		f = 0;
	}

	e++;

	if (e != b) {
		goto L11;
	}

	d++;
	if (d != b) {
		goto L10;
	}

	if (f == 0) {
		h -= -1;
		/* printf("Intermedit: %ld\n", h); */
	}

	if (b == c) {
		/* printf("%ld\n", h); */
		return h;
	}

	/* sub b -17 */
	b -= -17;
	/* jnz 1 -23 */
	goto L8;
}

int main() {

	printf("Solve: %ld\n", solve());
}


