import cv2
import sys
def cut_face(inputlist, outputpath):
    '''
        OpenCVを用いて顔検出を行い、検出した場合顔を抽出します。
        引数1:画像のパスが入っているファイル
        引数2:出力先ディレクトリ
    '''
  #顔認識用のパス
  cascade_path = "./../envs/tensorflow/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
  f = open(inputlist)
  pathlist = f.readlines()
  f.close()
  count = 0

  for path in pathlist:
    count = count + 1
    #ファイル読み込み
    #readlinesは改行まで読んでしまうので改行削除
    path = path[:-1]
    image = cv2.imread(path)

    #グレースケール変換
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #顔認識用のカスケード指定
    cascade = cv2.CascadeClassifier(cascade_path)

    #顔認識の実行
    facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.2, minNeighbors=2, minSize=(30, 30))

    # 検出した場合
    if len(facerect) > 0:
        #顔を切り取り
        for (x,y,w,h) in facerect:
            face = image[y:y+h, x:x+w]
            file_name = outputpath + str(count) + ".jpg"
            cv2.imwrite(file_name, face )
    else:
        print("not count")

if __name__ == '__main__':
    # 入力の読み込み
    if len(sys.argv) < 3:
        print("argv is short")
        exit()
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
    cut_face(input_path, output_path)
