from cicd_templates_c265e2ef.common import Job


class SampleJob(Job):
    def launch(self):
        self.logger.info("Launching bootstrap job")

        df = self.spark.range(0, 1000)

        df.write.format(self.conf["output_format"]).mode("overwrite").save(self.conf["output_path"])

        self.logger.info("Bootstrap job finished!")

if __name__ == "__main__":
    job = SampleJob()
    job.launch()
