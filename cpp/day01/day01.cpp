#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <unordered_set>

#include "reader.hpp"


using namespace std;

int main()
{
    // ifstream ifs("input.txt", ifstream::in);
    // auto lines = vector<string>(read_input(ifs));
    
    // Part 1 - parse input to ints and return total value
   
    
    
    auto target = 30000000;
    // inputs = 0,3,6
    // Part 2
    // compute partial sums, as each freq is increased by freq in each round, cyclic
    vector<uint32_t> lut(target,-1);
    auto last = 6;
    lut[3] = 1;
    lut[0] = 0;
    for (auto i = 3;i<target; i++) {
        // new
        if (lut[last] == -1) {
            lut[last] = i-1;
            last = 0;
        }
        else{
            auto d = i-1-lut[last];
            lut[last] = i-1;
            last = d;
        }
    }
    cout << last << endl;
    
    
    
    
}