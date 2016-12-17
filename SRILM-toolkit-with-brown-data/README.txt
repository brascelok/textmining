I. SETUP SRILM

1. Installing CYQWIN:
Phải có các package sau: “binutils”, “gawk”, “gcc”, “gzip”, “make”, “tcltk”, “tcsh”

2. Installing SRILM
Download từ http://www.speech.sri.com/projects/srilm/download.html , được file srilm-1.7.2.tar.gz

3. Config CYQWIN
- Mở Cygwin Termina, gõ lệnh sau:
	$ cd /
	$ mkdir srilm  // tạo thư mục tên ‘srilm’
	$ cd srilm

- Copy file ‘srilm-1.7.1.tar.gz’ vào đường dẫn ‘C:\cyqwin64\srilm’ (nếu máy là 64bit). Sau đó giải nén bằng dòng sau:
	$ tar zxvf srilm-1.7.1.tar.gz

- Vào ‘C:\cygwin64\home\yourname\.bashrc’, thêm mấy dòng sau vào đầu file rồi save lại:
	export SRILM=/srilm
	export MACHINE_TYPE=cyqwin
	export PATH=$PATH:$pwd:$SRILM/bin/cygwin
	export MANPATH=$MANPATH:$SRILM/man
	
- Restart Cyqwin

4. Setup package
Sau khi download về, cần copy các package từ Cygwin vao srilm
- Tìm thư mục có tên như http%3a%2f%2fcygwin.mirror.constant.com%2f (thư mục này được chọn lúc download các package của Cygwin)
	Ví dụ: C:\Users\brascelok\Downloads\Programs\http%3a%2f%2fcygwin.mirror.constant.com%2f
- Tìm các package sau:
	binutils-2.25-4.tar.xz
	gawk-4.1.3-1.tar.xz
	gcc-core-4.9.3-1.tar.xz
	gcc-g++-4.9.3-1.tar.xz
	gzip-1.6-1.tar.xz
	make-4.1-1.tar.xz
	tcl-8.5.18-1.tar.xz
	tcl-devel-8.5.18-1.tar.xz
	tcl-tk-8.5.18-1.tar.xz
	tcl-tk-devel-8.5.18-1.tar.xz
	tcsh-6.19.00-2.tar.xz
	
	(Một số package ko có, thì lại vào lại file cài của CYQWIN để chọn cài. nhưng cách nhanh nhất là seach google theo tên file còn thiếu download về cho nhanh)
Sau đó copy hết các package trên vào C:\cygwin64\srilm
- Vào lại Cygwin Termina, giải nén hết các package ra 
	Ví dụ: $ tar xvf binutils-2.25-4.tar.xz
	
- Restart Cyqwin

5. Setup SRILM:
Vào ‘C:\cygwin64\srilm’, mở file ‘Makefile’, thêm vào dòng:

	SRILM = /srilm
	
Trong Cyqwin, di chuyển vào thư mục srilm và cài đặt:

$ cd /srilm
$ make World
$ make all
$ make cleanest

Ở đoạn ‘make World’, nếu xuất hiện lỗi,có dạng ‘Command not found’ hoặc ‘tcl.h do not exist’, thì cài đặt bổ sung các package đó rồi thử lại. 

Sau khi xong hết 3 command trên là đã cài thành công

II. LANGUAGE MODELING
1. Tạo vocab
Run file getVocabulary.py để đọc đọc các từ tập brown-train.txt (tự thay đổi path đến file trong code)
Sau khi chạy sẽ được file brown-train-vocab.txt

2. Run
- Copy 3 file brown-train.txt, brown-test.txt, brown-train-vocab.txt vào C:\cygwin64\srilm\bin\cygwin64
- Di chuyển tới srilm\bin\cygwin64 trong Cygwin Termina
- Chạy câu lệnh: 
	$ ngram-count -vocab brown-train-vocab.txt -text brown-train.txt -order 3 -write brown-train.count -unk
	>> được file brown-train.count
 
- Tiếp tục chạy câu lệnh: (Training the N-gram Language Model)
	$ ngram-count -vocab brown-train-vocab.txt -read brown-train.count -order 3 -lm brown-lm.lm -gt1min 3 -gt1max 7 -gt2min 3 -gt2max 7 -gt3min 3 -gt3max 7
	>> được file brown-lm.lm
- Calculating the Test Data Perplexity:
	$ ngram -ppl brown-test.txt -order 3 -lm brown-lm.lm
	
	>> KẾT QUẢ: 
	
	file brown-test.txt: 5735 sentences, 95429 words, 3379 OOVs
0 zeroprobs, logprob= -234557.5 ppl= 250.4413 ppl1= 353.3074

