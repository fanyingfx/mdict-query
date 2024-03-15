from pathlib import Path
from src.mdict_query.mdict_utils import MDXDict
MDX_FILE= "D:/Code/mdict-query/mdx/olad10/Oxford Advanced Learner's Dictionary 10th.mdx"
MDXPATH=Path(MDX_FILE)
if __name__=='__main__':

    mdx_dict= MDXDict(MDXPATH)
    res=mdx_dict.lookup('hello')
    file=mdx_dict.lookup('hello__gb_1.ogg')

    JP_MDX_FILE = 'C:/Users/fanzh/PycharmProjects/lute-backend/data/dicts/ja/Shogakukanjcv3/Shogakukanjcv3.mdx'
    JP_MDXPATH = Path(JP_MDX_FILE)
    jp_mdx_dict = MDXDict(JP_MDXPATH)
    res=jp_mdx_dict.lookup('ニュース')
    print(res.decode('utf-8'))


