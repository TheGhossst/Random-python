#include <stdio.h>
#include <stdlib.h>

#define SIZE 6 

typedef struct {
    char items[SIZE];
    int front, rear;
} CircularQueue;

void initializeQueue(CircularQueue* q) {
    q->front = -1;
    q->rear = -1;
    for (int i = 0; i < SIZE; i++) {
        q->items[i] = '-';
    }
}

int isFull(CircularQueue* q) {
    if ((q->front == 0 && q->rear == SIZE - 1) || (q->rear == (q->front - 1) % (SIZE - 1))) {
        return 1;
    }
    return 0;
}

int isEmpty(CircularQueue* q) {
    if (q->front == -1) {
        return 1;
    }
    return 0;
}

void enqueue(CircularQueue* q, char value) {
    if (isFull(q)) {
        printf("Queue is full\n");
        return;
    } else {
        if (q->front == -1) {
            q->front = 0;
        }
        q->rear = (q->rear + 1) % SIZE;
        q->items[q->rear] = value;
        printf("Inserted %c\n", value);
    }
}

char dequeue(CircularQueue* q) {
    if (isEmpty(q)) {
        printf("Queue is empty\n");
        return '-';
    } else {
        char value = q->items[q->front];
        while (value == '-') {
            q->front = (q->front + 1) % SIZE;
            if (q->front == q->rear) {
                q->front = -1;
                q->rear = -1;
                return '-';
            }
            value = q->items[q->front];
        }
        if (q->front == q->rear) {
            q->front = -1;
            q->rear = -1;
        } else {
            q->items[q->front] = '-'; 
            q->front = (q->front + 1) % SIZE;
        }
        return value;
    }
}

void displayQueue(CircularQueue* q) {
    if (isEmpty(q)) {
        printf("Queue is empty\n");
        return;
    }
    int i = q->front;
    while (1) {
        printf("%c ", q->items[i]);
        if (i == q->rear) {
            break;
        }
        i = (i + 1) % SIZE;
    }
    printf("\n");
}

int main() {
    CircularQueue q;
    initializeQueue(&q);

    enqueue(&q, 'd');
    enqueue(&q, '-');
    enqueue(&q, '-');
    enqueue(&q, 'a');
    enqueue(&q, 'b');
    enqueue(&q, 'c');
    printf("Initial queue: ");
    displayQueue(&q);

    printf("Deleted %c\n", dequeue(&q));
    printf("Deleted %c\n", dequeue(&q));
    printf("Queue after two deletions: ");
    displayQueue(&q);

    enqueue(&q, 'x');
    enqueue(&q, 'y');
    enqueue(&q, 'z');
    printf("Queue after three additions: ");
    displayQueue(&q);

    printf("Final front position: %d\n", q.front+1);
    printf("Final rear position: %d\n", q.rear+1);

    return 0;
}
