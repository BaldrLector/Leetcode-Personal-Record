class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
		vector<vector<string>> result;
		unordered_map<string, vector<string>> map;
        for(string str : strs){
			string copy = str;
			sort(str.begin(), str.end());
			map[str].push_back(copy);
		}
		
		for(auto it = map.begin(); it != map.end(); ++it){
			result.push_back(it->second);
		}
		return result;
    }
};