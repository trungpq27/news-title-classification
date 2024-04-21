2-1) Chuẩn bị dữ liệu 

Tải xuống bộ dữ liệu News Aggregator Data Set, tạo ra dữ liệu huấn luyện (train.txt), dữ liệu kiểm chứng (valid.txt) và dữ liệu đánh giá (test.txt) theo hướng dẫn dưới đây.
Giải nén file zip đã tải xuống, đọc hướng dẫn của file readme.txt
Trích xuất ra các example (bài báo) của các báo "Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail".
Sắp xếp lại các example đã trích xuất theo thứ tự ngẫu nhiên.
Phân chia các example đã trích xuất với tỉ lệ 80% cho tập train, còn lại dùng 10% cho tập kiểm chứng và 10% cho tập đánh giá và lưu thành các file train.txt, valid.txt, test.txt. Trong các file, mỗi dòng lưu một example, tên của category và title của các bài báo được phân cách bởi dấu tab. Các file này sau này sẽ được dùng lại trong các bài tập tiếp theo.

2-2) Khám phá dữ liệu 

Thực hiện các công việc sau:
Thống kê số samples cho từng label trong dữ liệu trong tập train, valid và test
Tính số lượng word trung bình, số lượng word lớn nhất, nhỏ nhất trong các samples trong tập train, valid, test

2-3) Huấn luyện mô hình phân loại 

Hãy huấn luyện mô hình phân loại văn bản trên dữ liệu train
Có thể sử dụng bất kỳ thuật toán phân loại văn bản nào mà bạn biết
Trong quá trình xây dựng mô hình phân loại văn bản, hãy sử dụng tập valid để lựa chọn siêu tham số (hyper-parameters)

2-4) Đánh giá mô hình phân loại 

Đánh giá mô hình phân loại mà bạn đã xây dựng ở bài 2-3) trên tập dữ liệu test. Tính các chỉ số precision, recall, F1 cho từng nhãn và các chỉ số trung bình (macro-average)

2-5) Triển khai mô hình phân loại thành API 

Hãy triển khai mô hình phân loại văn bản mà bạn đã xây dựng thành API theo đặc tả sau đây. Có các end-point như mô tả dưới đây.
Base URL: http://localhost:2005
2-5-1. Liệt kê danh sách các nhãn
API này sẽ liệt kê danh sách các nhãn (labels) trong tập nhãn.
End-point:
/list_label
Method: GET
Request body
Request parameters: NONE
Respone

JSON Key
Type
Description
labels
list
Danh sách các label có trong mô hình

2-5-2. Phân loại văn bản
API này nhận đầu vào là một đoạn text và trả ra label của nhãn đó cùng với xác suất (confidence score) tương ứng.

/classify
Method: POST

Parameters

Name
Type
Description
text
string
Nội dung text đầu vào

Respone

JSON Key
Type
Description
text
string
Nội dung input text
predicted_label
string
Nhãn dự đoán
prob
float
Xác suất của nhãn dự đoán

