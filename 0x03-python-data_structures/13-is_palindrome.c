#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks whether a list is a palindrome
 * @head: point to first elements pointer
 * Return: 1 if palindrome, else 0
 * empty list is considered a palindrome
 * consider two people fast and slow reading through list
 * the fast one read two nums at a time and the slow 1
 * by the time the faster one finishes the other will be
 * halfway through.
 * reverse the second half from the middle
 * compare the first half and the second
 * if thwy match totally it is a palindrome else not
 */

int is_palindrome(listint_t **head)
{
        listint_t *fast, *slow, *temp, *second_half;

        temp = malloc(sizeof(listint_t));
        if (temp == NULL)
                return (0);

        if (*head == NULL || (*head)->next == NULL)
                return (1);

        fast = *head;
        slow = *head;
        second_half = NULL;

        while (fast != NULL && fast->next != NULL)
        {
                slow = slow->next;
                fast = fast->next->next;
        }

        /**
         * separater the two halves
         */
        temp->next = NULL;

        while (slow != NULL)
        {
                temp = slow->next;
                slow->next = second_half;
                second_half = slow;
                slow = temp;
        }
        while (*head != NULL && second_half != NULL)
        {
                if ((*head)->n != second_half->n)
                        return (0);

                *head = (*head)->next;
                second_half = second_half->next;
        }
        return (1);
}
