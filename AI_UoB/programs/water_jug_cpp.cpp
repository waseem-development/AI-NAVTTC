#include <iostream>
#include <iomanip>
#define LIMIT 1000
int capacityOfJugA, capacityOfJugB;

void displayStatus(int stepNumber, int a, int b);
int findMinimum(int val1, int val2);
int findSolution(int n, int &steps);

int main()
{
    while (true)
    {
        int required, steps = 0;
        std::cout << "Enter the Capacity of Jug A: ";
        std::cin >> capacityOfJugA;
        std::cout << "Enter the Capacity of Jug B: ";
        std::cin >> capacityOfJugB;
        std::cout << "Water Required to be filled in Jug B: ";
        std::cin >> required;

        if (capacityOfJugB < required)
        {
            std::cerr << "\n\nError: " << required << " liter(s) cannot be adjusted in Jug B of "
                      << capacityOfJugB << " liter(s)\n";
        }
        else if ((capacityOfJugA == capacityOfJugB) && (capacityOfJugB != required))
        {
            std::cout << "\n\nError! Invalid Input Values\n";
        }
        else
        {
            if (findSolution(required, steps))
            {
                std::cout << "\n\nCalculated Solution Taken in " << steps << " step(s)\n\n*********************************************\n\n";
            }
            else
            {
                std::cout << "\n\nSorry. Unable to calculate the result even after "
                          << steps << " steps.\n*********************************************\n\n";
            }
        }
    }

    return 0;
}

void displayStatus(int stepNumber, int a, int b)
{
    std::cout << std::setw(10) << stepNumber
              << std::setw(10) << a
              << std::setw(10) << b << "\n";
}

int findMinimum(int val1, int val2)
{
    return (val1 < val2) ? val1 : val2;
}

int findSolution(int n, int &steps)
{
    int a = 0, b = 0, step = 0, temp = 0;
    std::cout << "\n"
              << std::left
              << std::setw(18) << ""
              << std::setw(10) << "Step # "
              << std::setw(10) << "Jug A"
              << std::setw(10) << "Jug B"
              << "\n";

    while ((b != n) && (step < LIMIT))
    {
        step++;
        if (a == 0)
        {
            a = capacityOfJugA;
            std::cout << std::setw(20) << "Fill A";
            displayStatus(step, a, b);
        }
        else if (b == capacityOfJugB)
        {
            b = 0;
            std::cout << std::setw(20) << "Empty Jug B";
            displayStatus(step, a, b);
        }
        else
        {
            temp = findMinimum(capacityOfJugB - b, a);
            b = b + temp;
            a = a - temp;
            std::cout << std::setw(20) << "Pour A in B";
            displayStatus(step, a, b);
        }
    }
    steps = step;
    return (steps == LIMIT) ? 0 : 1;
}