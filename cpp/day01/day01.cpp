/*
Advent of Code 2021 - Day 01
[https://adventofcode.com/2021/day/1]

*/
#include <bits/stdc++.h>
#include "reader.hpp"

using namespace std;

std::vector<std::string> split(const std::string &str, const char &delim = ',')
{
    std::stringstream ss(str);
    std::string token;
    std::vector<std::string> toks;
    while (std::getline(ss, token, delim))
    {
        toks.push_back(token);
    }
    return toks;
}

int main()
{
    
    // Part 1 - parse input to ints and return total value

    string input_file = "../../inputs/day01.txt";
    ifstream ifs(input_file, ifstream::in);
    auto input_lines = vector<string>(read_input(ifs));
    vector<int> input(2, INT_MAX);
    transform(input_lines.begin(), input_lines.end(), back_inserter(input),
              [](const string &s)
              { return stoi(s); });

    
    // Part1 & Part2
    auto it = input.begin() + 3;
    int part1(0), part2(0);
    for (; it != input.end(); it++)
    {
        part2 += (*it > *(it - 3) ? 1 : 0);
        part1 += (*it > *(it - 1) ? 1 : 0);
    }
    cout << "Advent of Code 2021 - Day 01\n\n";
    cout << "Part 1:\t"<< part1 << "\n" << "Part 2:\t"<<part2 << endl;

}