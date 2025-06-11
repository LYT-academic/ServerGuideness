```bash
>>> sinfo -p cluster_long -N -o "%N %m"

NODELIST MEMORY
cc21cluster20 385428
cc21cluster21 385428
cc21cluster22 385428
cc21cluster23 385428
cc21cluster24 385428
cc21cluster25 385428
cc21cluster26 385428
cc21cluster27 385428
cc21cluster28 385428
cc21cluster29 385428
cc21cluster30 385428
cc21cluster31 385428
cc21cluster32 385428
cc21cluster33 385428
cc21cluster34 385428
cc21cluster35 385428
cc21cluster36 385428
cc21cluster37 385428
```

## Check running memory for nodes
```bash
# 3509739 is JobID
>>> sstat -p 3509739 --allsteps --format=JobID,MaxRSS,AveRSS

JobID|MaxRSS|AveRSS|
3509739.extern|4K|4K|
3509739.batch|61391672K|48099040K|

# .extern is slurm process, .batch is our task  
sstat -p 3509739.batch --allsteps
▶ sstat -p 3509739.batch --allsteps 
JobID|MaxVMSize|MaxVMSizeNode|MaxVMSizeTask|AveVMSize|MaxRSS|MaxRSSNode|MaxRSSTask|AveRSS|MaxPages|MaxPagesNode|MaxPagesTask|AvePages|MinCPU|MinCPUNode|MinCPUTask|AveCPU|NTasks|AveCPUFreq|ReqCPUFreqMin|ReqCPUFreqMax|ReqCPUFreqGov|ConsumedEnergy|MaxDiskRead|MaxDiskReadNode|MaxDiskReadTask|AveDiskRead|MaxDiskWrite|MaxDiskWriteNode|MaxDiskWriteTask|AveDiskWrite|TRESUsageInAve|TRESUsageInMax|TRESUsageInMaxNode|TRESUsageInMaxTask|TRESUsageInMin|TRESUsageInMinNode|TRESUsageInMinTask|TRESUsageInTot|TRESUsageOutAve|TRESUsageOutMax|TRESUsageOutMaxNode|TRESUsageOutMaxTask|TRESUsageOutMin|TRESUsageOutMinNode|TRESUsageOutMinTask|TRESUsageOutTot|
3509739.batch|61800304K|cc21cluster25|0|48350740K|61391672K|cc21cluster25|0|48102112K|1.50K|cc21cluster25|0|1.50K|24-12:52:11|cc21cluster25|0|24-12:52:11|1|1K|0|0|0|0|10576253|cc21cluster25|0|10576253|31828|cc21cluster25|0|31828|cpu=24-12:52:11,energy=0,fs/disk=10576253,mem=48102112K,pages=1.50K,vmem=48350740K|cpu=24-12:52:11,energy=0,fs/disk=10576253,mem=61391672K,pages=1.50K,vmem=61800304K|cpu=cc21cluster25,energy=cc21cluster25,fs/disk=cc21cluster25,mem=cc21cluster25,pages=cc21cluster25,vmem=cc21cluster25|cpu=00:00:00,fs/disk=0,mem=0,pages=0,vmem=0|cpu=24-12:52:11,energy=0,fs/disk=10576253,mem=61391672K,pages=1.50K,vmem=61800304K|cpu=cc21cluster25,energy=cc21cluster25,fs/disk=cc21cluster25,mem=cc21cluster25,pages=cc21cluster25,vmem=cc21cluster25|cpu=00:00:00,fs/disk=0,mem=0,pages=0,vmem=0|cpu=24-12:52:11,energy=0,fs/disk=10576253,mem=48102112K,pages=1.50K,vmem=48350740K|energy=0,fs/disk=31828|energy=0,fs/disk=31828|energy=cc21cluster25,fs/disk=cc21cluster25|fs/disk=0|energy=0,fs/disk=31828|energy=cc21cluster25,fs/disk=cc21cluster25|fs/disk=0|energy=0,fs/disk=31828|
```
61391672K ≈ 58.5 GB
48099040K ≈ 45.87 GB
AveCPU = 24-12:52:11表示所有的CPU核累计使用时间，想知道实际使用了多少个cpu核运行，可以用 24天12小时52分11秒 = 588.5小时/18.5小时（该任务已运行时间）≈ 31.8≈32 core