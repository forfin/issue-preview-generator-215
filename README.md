## Reproduce .ai image problem

https://github.com/algoo/preview-generator/issues/215

### reproduce command
```
docker build . -t my-test && docker run my-test python app.py
```

### expected result
It return string of preview path

### actual result
```
Traceback (most recent call last):
  File "app.py", line 14, in <module>
    test_problem()
  File "app.py", line 10, in test_problem
    output = manager.get_jpeg_preview(file_path=PROBLEM_FILE, height=512, width=512, force=True)
  File "/usr/local/lib/python3.7/site-packages/preview_generator/manager.py", line 186, in get_jpeg_preview
    mimetype=preview_context.mimetype,
  File "/usr/local/lib/python3.7/site-packages/preview_generator/preview/builder/image__pillow.py", line 255, in build_jpeg_preview
    result = self.image_to_jpeg_pillow(img, size)
  File "/usr/local/lib/python3.7/site-packages/preview_generator/preview/builder/image__pillow.py", line 270, in image_to_jpeg_pillow
    with Image.open(png) as image:
  File "/usr/local/lib/python3.7/site-packages/PIL/Image.py", line 2959, in open
    "cannot identify image file %r" % (filename if filename else fp)
PIL.UnidentifiedImageError: cannot identify image file <_io.BufferedReader name='/home/app/problem.ai'>
```