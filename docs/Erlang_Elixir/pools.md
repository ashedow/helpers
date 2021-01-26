# Pools types

## 1
Необходим параллельный доступ к ресурсам и состояниям

Round robin, Random routing

Быстро выбирают один процесс, но не гарантирует что сообщение попадет в свободный процесс

## 2 
Необходимо выдавать ограниченный ресурс на использование. Например коннект к БД

Checkout pool

Гарантирует что сообщение попадет в свободные процессы

## Размеры пула

## 1
Доступ к ресурсу ограничен, например коннекшн  к бд

Static - 

размер пула константный, сообщения могут попасть в занятый процесс

## 2

Нашрузка на пул меняется, напрм кол-во сокетов

Dynamic

Размер пула динамические новое сообщение в свободный процесс

## Распределенность

## пуллы процессов

Для пуллв процессов нужно уметь:
* Создавать процесы     Supervisor
* контролировать падения    Supervisor
* контролировать количество    Supervisor
* обращаться к процессам    Registration
* обращаться по выбранной стратегии    Registration

supervisor, manger, registry, pool supervisor

poolboy lib
nimblePool - lib для checkout пуллов от создателей elixir
horde & Swarm - libs hfcghtltktyyst cegthdbpjhs b registry построенны на CRDT, eventually consistent
gproc syn pg pg2 pheonix_pubsub  - группы процессов и некоторые предоставляют роутинг
 ranch global consuela dbconnection finch magita machinegun hackney - пуллы и системы регистрации для конкретной задачи


## links
https://www.youtube.com/watch?v=rpGxmti3rhw
https://andrealeopardi.com/posts/process-pools-with-elixirs-registry/

