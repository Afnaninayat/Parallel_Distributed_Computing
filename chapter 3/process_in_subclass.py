/*************  ✨ Codeium Command 🌟  *************/
Added a subclass of multiprocessing.Process that overrides the run method
import multiprocessing

class MyProcess(multiprocessing.Process):

    def run(self):
        print ('called run method in %s' %self.name)
        return

if __name__ == '__main__':
    for i in range(10):
        process = MyProcess()
        process.start()
        process.join()

/******  3dd4c128-4033-4992-bfc7-f4f8aa27cced  *******/