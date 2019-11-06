import os
import shutil

print(os.unlink("./delete.txt"))
print(os.rmdir("./empty"))
print(shutil.rmtree("./test", ignore_errors=True))