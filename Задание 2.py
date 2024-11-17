
def coin_toss_experiment(num_tosses):
    heads = 0
    tails = 0

    # Подбрасываем монетку заданное количество раз
    for _ in range(num_tosses):
        if random.choice(['орел', 'решка']) == 'орел':
            heads += 1
        else:
            tails += 1

    return heads, tails


def main():
    results = []

    # Выполняем эксперименты с разным количеством подбрасываний
    for num_tosses in [10, 100, 1000, 10000, 100000, 1000000]:
        heads, tails = coin_toss_experiment(num_tosses)
        ratio = min(heads, tails) / max(heads, tails)
        results.append((num_tosses, heads, tails, ratio))

    # Выводим результаты
    print("Количество подбрасываний | Орлы | Решки | Отношение (меньшее/большее)")
    for num_tosses, heads, tails, ratio in results:
        print(f"{num_tosses:<24} | {heads:<5} | {tails:<5} | {ratio:.6f}")


if __name__ == "__main__":
    main()