import time
import logging
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler(r'C:\Users\IT ZONE_PC\Documents\AI_Employee_Vault\Logs\watcher.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

VAULT = Path(r'C:\Users\IT ZONE_PC\Documents\AI_Employee_Vault')
NEEDS_ACTION = VAULT / 'Needs_Action'
DROP_FOLDER = VAULT / 'Drop_Here'

class DropFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        source = Path(event.src_path)
        dest = NEEDS_ACTION / source.name
        shutil.copy2(source, dest)
        logger.info(f'[NEW FILE] {source.name} -> Needs_Action')
        md_file = NEEDS_ACTION / f'TASK_{source.stem}.md'
        md_file.write_text(f'''---
type: file_task
file_name: {source.name}
received: {time.strftime('%Y-%m-%d %H:%M:%S')}
status: pending
---

## Naya File Mila!
**File:** {source.name}

## Claude ke liye Tasks
- [ ] File ko check karo
- [ ] Agar invoice hai toh Accounting mein log karo
- [ ] Summary banao
- [ ] Dashboard update karo
- [ ] Move to /Done jab complete ho
''', encoding='utf-8')
        logger.info(f'[TASK CREATED] TASK_{source.stem}.md')

def main():
    logger.info('=== AI Employee Watcher Shuru Ho Gaya ===')
    logger.info(f'Monitoring: {DROP_FOLDER}')
    handler = DropFolderHandler()
    observer = Observer()
    observer.schedule(handler, str(DROP_FOLDER), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
        logger.info('=== Watcher Band Ho Gaya ===')
    observer.join()

if __name__ == '__main__':
    main()
