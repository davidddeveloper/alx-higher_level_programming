#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a linked list is read the same backward or forward
 * @head: points to the start of the linked list
 * Return: 0 if it is not a palindrome
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *list = *head, *new_rev_list = NULL, *instance_two, *new_node;

	/* Create a reversed copy of the list */
	while (list != NULL)
	{
		new_node = malloc(sizeof(listint_t));
		new_node->n = list->n;
		new_node->next = new_rev_list;
		new_rev_list = new_node;

		list = list->next;
	}

	list = *head;
	instance_two = new_rev_list;
	/* Checks if the list is a palindrome */
	while (list != NULL && instance_two != NULL)
	{
		if (list->n != instance_two->n)
		{
			/* clean up the dynamically allocated memory */
			while (new_rev_list != NULL)
			{
				new_node = new_rev_list;
				new_rev_list = new_rev_list->next;
				free(new_node);
			}
			return (0); /* It is not a palindrome */
		}
		list = list->next;
		instance_two = instance_two->next;
	}
	/* Clean up the dynamically allocated memory */
	while (new_rev_list != NULL)
	{
		new_node = new_rev_list;
		new_rev_list = new_rev_list->next;
		free(new_node);
	}
	return (1); /* It is a palindrome */
}
