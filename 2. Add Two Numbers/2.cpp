/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode preHead(0), *p = &preHead;
        int r = 0;
        while (l1 || l2 || r) {
            if (l1) r += l1->val, l1 = l1->next;
            if (l2) r += l2->val, l2 = l2->next;
            p->next = new ListNode(r % 10);
            r /= 10;
            p = p->next;
        }
        return preHead.next;
    }
};