class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size() <= 1)
            return s;
        int left_index = 0;
        int max_length = 0;
        const int string_size = s.size();
        for(int i = 1; i < string_size; ++i)
        {
            int search_left = i;
            int search_right = i;
            const char current_char = s[i];
            // left repeat
            for(int j = i-1; j >= 0; --j)
            {
                if(s[j]==current_char)
                    --search_left;
                else
                    break;
            }
            // right repeat
            for(int j = i+1; j < string_size; ++j)
            {
                if(s[j]==current_char)
                    ++search_right;
                else
                    break;
            }

            // search both left and right
            while((search_left - 1) >= 0 && (search_right + 1) < string_size)
            {
                const char left = s[search_left-1];
                const char right = s[search_right+1];
                if(left != right)
                    break;
                --search_left;
                ++search_right;
            }
            // if length is greater, record indexes
            const int current_length = search_right - search_left + 1;
            if(current_length > max_length)
            {
                max_length = current_length;
                left_index = search_left;
            }
        }
        return s.substr(left_index, max_length);
    }
};
