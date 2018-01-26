class Solution {
public:
	vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
		vector< vector< vector<int> > > combinations(target + 1, vector<vector<int>>());
		combinations[0].push_back(vector<int>());
		for (auto& score : candidates)
			for (int j = score; j <= target; j++)
				if (combinations[j - score].size() > 0)	{
					auto tmp = combinations[j - score];
					for (auto& s : tmp)
						s.push_back(score);
					combinations[j].insert(combinations[j].end(), tmp.begin(), tmp.end());
				}
		auto ret = combinations[target];
		for (int i = 0; i < ret.size(); i++)
			sort(ret[i].begin(), ret[i].end());
		return ret;
	}
};