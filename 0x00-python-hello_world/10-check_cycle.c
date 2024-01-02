#include "lists.h"

/**
 * check_cycle - check for loop in LL
 * @list: head of linked list
 *
 * Description - check for loops in LL
 * Return: 1 if cycled, 0 if not
 * assume you are in a race with 2 cars
 * one slow and one fast car
 * depending on the race if circuit or sprint
 * if there are not set laps, the faster finishes first
 * if there are laps the faster car will overlap the slow
 * the race in this case represents the list
 * the lap represents loop
 * if there are no loops return 0 success
 * if there are loops, where the fast car may be same position
 * as the slow car, return 1 indicating cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
	{
		return (0);
	}
	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
