## Blackjack
#The BlackJack Game. Suporting languages: English
__________________________________________________________________________________________________________________________________________________________________________________
*Денчик, специально для тебя оставляю условия, как работает программка с моими допущениями. Надеюсь, увидишь.*
__________________________________________________________________________________________________________________________________________________________________________________

Итак, в начале нам и компьютеру дается по две карты, вторую карту компьютера мы не видим, только свои две, которые тебе и печатаются. После чего - игрок выбирает брать ли еще карту и так до тех пор, пока он не остановится, либо не перешагнет число 21, что считается проигрышем. После чего идет подсчет суммы очков игрока и компьютера и раскрываются карты второго и соответсвенно выдается результат, кто победил с предложением начать новую игру.
__________________________________________________________________________________________________________________________________________________________________________________
Несколько моих слов по коду:

1. Желательно запускать его в консоли, ибо там команда чистит консоль (*os.system('cls' if os.name == 'nt' else 'clear')*), я не знаю, как она работает в IDE-шках.
2. Там есть функции, я к ним не писал докстринги - смогу объяснить лично, если вдруг чего не поймешь.
3. Попробуй плз, поиграйся, мб словишь какой-то баг или я чего не заметил.
4. Если есть какие-то претензии по коду, то говори. Я просто хз - понятна ли моя логика/правильно ли ваще написано или перемудрил.
5. У меня в алгоритме есть такое условие, что компьютер не будет добирать карты, если у него сумма карт уже равна 16 и я не знаю - костыль это или нормальное решение, как думаешь?
__________________________________________________________________________________________________________________________________________________________________________________
**Обнял, приподнял.**
