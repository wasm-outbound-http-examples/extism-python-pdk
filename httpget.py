import extism

@extism.plugin_fn
def httpget():
  res = extism.Http.request('https://httpbin.org/anything')
  extism.output_str(res.data_str())
