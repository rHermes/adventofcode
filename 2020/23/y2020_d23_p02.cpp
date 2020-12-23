#include <list>
#include <vector>
#include <cstdio>
#include <iterator>

using namespace std;

int main() {
	/* vector<long> nums{3,8,9,1,2,5,4,6,7}; */
	vector<long> nums{9,1,6,4,3,8,2,7,5};
	
	
	vector<list<long>::iterator> pos(nums.size());
	list<long> ls;
	long max = 0;
	for (auto e : nums) {
		if (max < e) {
			max = e;
		}
		pos[e-1] = ls.insert(ls.end(), e);
	}

	for(int i = max+1; i < 1000000+1; i++) {
		pos.push_back(ls.insert(ls.end(), i));
	}
	long cur = nums[0];
	for (long i = 0; i < 10000000; i++) {
		auto elem = pos[cur-1];
		auto a = next(elem);
		auto b = next(a);
		auto c = next(b);

		long nextcc = *elem - 1;
		while (nextcc == 0 || nextcc == *a || nextcc == *b || nextcc == *c) {
			if (nextcc <= 1) {
				nextcc = pos.size();
			} else {
				nextcc -= 1;
			}
		}

		auto nn = pos[nextcc-1];
		ls.splice(next(nn), ls, a, next(c));
		cur = *(next(elem));
		ls.splice(ls.end(), ls, elem);
	}

	auto mm = pos[0];
	auto a = next(mm) == ls.end() ? ls.begin() : next(mm);
	auto b = next(a) == ls.end() ? ls.begin() : next(a);
	printf("%ld\n", (*a)*(*b));

	return 0;
}
