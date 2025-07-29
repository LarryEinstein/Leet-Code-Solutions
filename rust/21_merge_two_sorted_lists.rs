// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
}

struct Solution;

impl Solution {
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        match (list1, list2) {
            (None, None) => None,
            (Some(l1), None) => Some(l1),
            (None, Some(l2)) => Some(l2),
            (Some(mut l1), Some(mut l2)) => {
                if l1.val <= l2.val {
                    l1.next = Self::merge_two_lists(l1.next, Some(l2));
                    Some(l1)
                } else {
                    l2.next = Self::merge_two_lists(Some(l1), l2.next);
                    Some(l2)
                }
            }
        }
    }
}

// Helper function to create a linked list from a vector
fn create_linked_list(values: &[i32]) -> Option<Box<ListNode>> {
    if values.is_empty() {
        return None;
    }
    
    let mut head = Box::new(ListNode::new(values[0]));
    let mut current = &mut head;
    
    for &val in &values[1..] {
        current.next = Some(Box::new(ListNode::new(val)));
        current = current.next.as_mut().unwrap();
    }
    
    Some(head)
}

// Helper function to convert linked list to vector
fn linked_list_to_vec(head: &Option<Box<ListNode>>) -> Vec<i32> {
    let mut result = Vec::new();
    let mut current = head;
    
    while let Some(node) = current {
        result.push(node.val);
        current = &node.next;
    }
    
    result
}

fn main() {
    // Create test linked lists
    let l1 = create_linked_list(&[1, 2, 4]);
    let l2 = create_linked_list(&[1, 3, 4]);
    
    println!("List 1: {:?}", linked_list_to_vec(&l1));
    println!("List 2: {:?}", linked_list_to_vec(&l2));
    
    // Merge the lists
    let merged = Solution::merge_two_lists(l1, l2);
    
    println!("Merged list: {:?}", linked_list_to_vec(&merged));
}