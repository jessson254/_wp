let scores = { Alice: 85, Bob: 92, Charlie: 78 };

for (let student in scores) 
{
    console.log(`${student} 的分數是 ${scores[student]}`);
}
