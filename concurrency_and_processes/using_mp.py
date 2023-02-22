import multiprocessing as mp
import time

def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        output.put(dish)

def dryer(input_d):
    while True:
        dish = input_d.get()
        print('Drying', dish, 'dish')
        time.sleep(0.3)
        input_d.task_done()

if __name__ == "__main__":
    mp.freeze_support()

    dish_queue = mp.JoinableQueue()

    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ['salad', 'bread', 'entree', 'dessert']

    washer(dishes, dish_queue)

    dish_queue.join()

