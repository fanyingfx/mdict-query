from pathlib import Path
from src.mdx_query.mdict_utils import MDXDict
MDX_FILE= "mdx/olad10/Oxford Advanced Learner's Dictionary 10th.mdx"
MDXPATH=Path(MDX_FILE)
if __name__=='__main__':

    mdx_dict= MDXDict(MDXPATH)
    res=mdx_dict.lookup('hello')
    file=mdx_dict.lookup('hello__gb_1.ogg')
    s=res.decode('utf8')
    print(s)

