import os
from stat import * # ST_SIZE etc
import subprocess
import re
import csv

class  FileList:
    def __init__(self, directoryPath):
        self.directoryPath = directoryPath #FileList object will hold directory path that is being searched
        self.filelist=[] #this will hold list of all found files
        self.skippedFiles=[] #this will hold files that were skipped while searching

    def filelength(self, filePath):
        process = subprocess.Popen(['ffmpeg',  '-i', filePath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = process.communicate()
        matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout, re.DOTALL).groupdict()

        #print process.pid
        process.kill()
        duration = {'hours': matches['hours'], 'minutes' : matches['minutes'], 'seconds' : matches['seconds'], 'total_in_sec' : float(matches['seconds']) + 60 * float(matches['minutes']) + 3600 * float(matches['hours'])}
        return duration

    def scanDirectory(self, allowedFormats):

        #convert allowedFormats to lower case (self.fileFormat will also be converted)
        #we need to do so because "mp4" != "MP4"
        [x.lower() for x in allowedFormats]


        for path, dirs, files in os.walk(self.directoryPath):
            for f in files:
                #Try reading stats of the file (Absoulte path) if it doesn't fail then we can continue parsing
                try:
                    self.absolutePath = path + '\\' + f
                    self.st=os.stat(self.absolutePath)
                    self.fileName_split = f.split(".")
                    self.fileFormat = self.fileName_split[-1]

                except IOError:
                    print "Failed to get information", f
                except:
                    print "Error reading file info or getting file format"
                else:
                    #There was no error reading filename, so we can continue parsing files
                    if self.fileFormat.lower() in allowedFormats:
                        try:
                            self.duration = self.filelength(self.absolutePath)
                        except Exception as inst:
                            print type(inst)     # the exception instance
                            print inst           # __str__ allows args to be printed directly
                            print "You are probably trying to get filelength of a file that isn't a video file. Hence ffmpeg fails."
                        else:
                            #There was no error reading movie file so we can update metadata
                            duration_string = "[%s:%s:%s]" % (self.duration['hours'],self.duration['minutes'],self.duration['seconds'])

                            self.metadata = {'fullpath' : self.absolutePath ,
                                        'filename' : f ,
                                        'format' : self.fileFormat,
                                        'filelength' :  duration_string,
                                        'filesize' : self.st[ST_SIZE],
                                        'ratio' : (self.duration['total_in_sec'] / self.st[ST_SIZE]) * 1000*1000}
                                        #time/size ratio, *1000 to convery bytes to kilobytes and then *1000 to scale the ratio to whole numbers
                                        # 0-4 bad, 4-6 not good, 6-8 good, 8> great
                            self.filelist.append(self.metadata)
                            print self.metadata
                    else:
                        self.metadata_skipped = {'fullpath' : self.absolutePath, 'format' : self.fileFormat}
                        self.skippedFiles.append(self.metadata_skipped)

    def dataOutput(self, filelist):
        self.writer = csv.writer(open('dict.csv', 'wb'))
        self.writer.writerow(["number of files", filelist.__len__()])

        for i in filelist: #filelist contains dictionaries with metadata about movie file
            for key, value in i.items(): #take each pair: [key,value] in dictionary i.items returns all the [key,value] pairs
                self.writer.writerow([key, value]) #write each [key,value] pair as a single line, separate them with comma

            self.writer.writerow("")#write blank line to separate each dictionary (so each file metadata)


if __name__ == "__main__":
    my_FileList = FileList("C:\Movies")
    my_FileList.scanDirectory(["mp4", "mkv", "flv", "wmv", "avi", "mpg", "mpeg"])
    my_FileList.dataOutput(my_FileList.filelist)
