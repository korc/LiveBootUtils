class NotAufs(ValueError): pass
class NotLoopDev(ValueError): pass
class NotSFS(ValueError): pass

        if not self.validate_sfs(): raise NotSFS("Not a SFS file", self.path)
        if not self.fs_type=="aufs": raise NotAufs("Mountpoint is not aufs", self.path)
        for branch_file in sorted(glob.glob(glob_prefix + "[0-9]*"), key=lambda v: int(v[len(glob_prefix):])):
        if not loop_name.startswith("loop"): raise NotLoopDev("Mountpoint does not seem to be loop device", loop_name)
    if d[:4]!="hsqs": raise NotSFS("file does not have sqsh signature")