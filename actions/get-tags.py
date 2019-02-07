from watson_developer_cloud import VisualRecognitionV3

def main(params):
    # init visual recognition library
    apiKey = params['apiKey']
    version = params['version']
    visual_recognition = VisualRecognitionV3(version=version, iam_apikey=apiKey)

    # get image url from params
    image_url = params['imageUrl']

    # parse visual recognition return data for our tags
    tags = ""
    classifiedImages = visual_recognition.classify(url=image_url).get_result()
    image = classifiedImages['images'][0]
    classes = image['classifiers'][0]['classes']
    for theClass in classes:
        currentTag = theClass['class']
        print(currentTag)
        tags = tags + currentTag + ", "
    result = {'classes': tags}
    return result
