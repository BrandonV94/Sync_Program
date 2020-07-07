# Program used to sync or at least copy files from one folder to another.
import os, shutil

os.chdir('/Users/brandon/testdir/Test1')
print('Checking source directory...')
dirListSrc = os.listdir()
print('First directory has: ', dirListSrc)
os.chdir('/Users/brandon/testdir/Test2')
print('Checking destination directory...')
dirListDes = os.listdir()
print('Second directory has: ', dirListDes)

for i in dirListSrc:
    for j in dirListDes:
        if(i == j):
            print(i, ' has the same name as ', j)
            ans = input('Would you like to remove and replace the file? Y/N)')
            if(ans == 'Y' or 'y'):
                os.remove(j)
            else:
                break;
shutil.copytree('/Users/brandon/testdir/Test1', '/Users/brandon/testdir/Test2', dirs_exist_ok=True)
print('The files have been copied')

# check files in dirs
# check for any fies with the same name
# if same name check if any diff lines
# if so copy lines


#src = 'Test1'
#des = 'Test2'
#shutil.copytree(src,des, dirs_exist_ok=True)
