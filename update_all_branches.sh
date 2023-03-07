
date >> history.log
echo "bash update_all_branches.sh\n" >> history.log
git add history.log && git commit -m 'update history log'

export BASE_BRANCH=no_data
git checkout ${BASE_BRANCH}

for BRANCH_NAME in 'icrush'\
 '711609' '729203' '724924' 'make-it-clear' \
 '652201' 'guilv' '726559' 'EmirKusturica' \
 '702958' '689047' 'kuakua' '733413'\
  '687802' '732302'
do
    echo '${BRANCH_NAME}'
    git checkout ${BRANCH_NAME} && git merge ${BASE_BRANCH} --no-edit && git pull && git push
done




# crush             装修灵感图库，              第三者视角观察自己，
# 亲密关系修复互助会   有一条无论如何都想沙一沙的龙  意难平小组
# 我发现个规律        围观工作党的爱情            佳片推荐
# 哄对象太难了吧      ta说这话什么意思            相互表扬小组
# 中二往事回忆录      不知道如何回复              我今天crush了没有回应