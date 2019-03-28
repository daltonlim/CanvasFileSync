import os
import urllib.request
import json

beginning = 'https://canvas.auckland.ac.nz/api/v1/courses/'
access_token = ''
ending = '?access_token=' + access_token + '&per_page=100'
courses = ['39993', '39854', '38455']


def getFolderName(folderId):
    folderUrl = beginning + course + '/folders/' + str(folderId) + ending
    json_object = getJsonObject(folderUrl)
    folderName = json_object['full_name']
    return folderName[13:]


def createFolder(folderName):
    try:
        os.mkdir(os.getcwd() + '/' + folderName)
    except:
        pass


def getJsonObject(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        x = json.loads(html)
        return x


def getCourseCode(courseId):
    json_object = getJsonObject(beginning + courseId + ending)
    return json_object['course_code']


for course in courses:
    courseCode = getCourseCode(course)
    x = getJsonObject(beginning + course + '/files' + ending)
    for json_object in x:
        folderName = getFolderName(json_object['folder_id'])

        createFolder(courseCode)
        createFolder(courseCode + '/' + folderName + '/')

        file = os.getcwd() + '/' + courseCode + '/' + folderName + '/' + json_object['display_name']

        if not os.path.isfile(file):
            urllib.request.urlretrieve(json_object['url'], file)
            print('downloading')

print('finished')
