import subprocess
import webbrowser

"""
This program uses Windows Powershell to generate a list of all the instealled programs
"""

"""
Uses a powershell comamand to generate and display in the terminal the list of installed programs
Also makes a txt file of the program list in the current directory called program_list.txt
"""
def generateProgramList():
    # The command to get the names of all installed programs
    file_gen_command = r"Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName | Format-Table -AutoSize"
    # Executes the command
    program_list = subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe',
                                  file_gen_command],
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    # convert the list to a string
    decoded_result = program_list.stdout.decode("ISO-8859-1").split("\n")[3:]
    # make file to display information along with the terminal
    filename = "program_list.txt"
    list_output_file = open(filename, "w+")

    # if the line isn't empty, add the line to the file and print it out
    try:
        for line in decoded_result:
            if len(line) > 0:
                if line[0] != " ":
                    line = line.strip()
                    print(line)
                    line = line + "\n"
                    list_output_file.write(line)
    except:
        pass
    list_output_file.close()

"""
Opens the list of programs txt file in notepad
"""
def openInNotepad():
    webbrowser.open("program_list.txt")
    input("Press enter to exit")

def main():
    generateProgramList()
    openInNotepad()

main()